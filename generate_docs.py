#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


MODULE_ORDER = [
    "oscfar",
    "oscfar-cfar",
    "oscfar-cluster",
    "oscfar-filters",
    "oscfar-gaussian_fit",
    "oscfar-reload",
    "oscfar-setup",
    "oscfar-utils",
]

DOC_TARGETS = {
    "oscfar": {"file": "oscfar.md", "title": "General functions", "nav_order": 1},
    "oscfar-cfar": {
        "file": "oscfar-cfar.md",
        "title": "CFAR Algorithms",
        "nav_order": 2,
    },
    "oscfar-filters": {
        "file": "oscfar-filters.md",
        "title": "Filtering",
        "nav_order": 3,
    },
    "oscfar-cluster": {
        "file": "oscfar-cluster.md",
        "title": "Clustering",
        "nav_order": 4,
    },
    "oscfar-gaussian_fit": {
        "file": "oscfar-gaussian.md",
        "title": "Fitting",
        "nav_order": 5,
    },
    "oscfar-utils": {"file": "oscfar-utils.md", "title": "Utilities", "nav_order": 6},
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Split python_docstring_markdown output into docs pages."
    )
    parser.add_argument(
        "input_file", type=Path, help="Path to generated markdown (temp.txt)"
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("docs"),
        help="Directory where docs markdown files are written",
    )
    return parser.parse_args()


def find_anchor_block(
    content: str, anchor: str, anchor_positions: dict[str, int]
) -> str:
    start = anchor_positions.get(anchor)
    if start is None:
        raise ValueError(f"Anchor '{anchor}' was not found in generated documentation.")

    next_pos = len(content)
    anchor_index = MODULE_ORDER.index(anchor)
    for next_anchor in MODULE_ORDER[anchor_index + 1 :]:
        candidate = anchor_positions.get(next_anchor)
        if candidate is not None and candidate > start:
            next_pos = candidate
            break

    return content[start:next_pos].strip() + "\n"


def normalize_module_block(block: str) -> str:
    lines = block.splitlines()

    module_heading_idx = next(
        (i for i, line in enumerate(lines) if line.startswith("## 🅼 ")), None
    )
    functions_heading_idx = next(
        (i for i, line in enumerate(lines) if line.strip() == "### Functions"), None
    )

    if module_heading_idx is not None:
        if (
            module_heading_idx + 1 >= len(lines)
            or lines[module_heading_idx + 1].strip() != "{: .no_toc }"
        ):
            lines.insert(module_heading_idx + 1, "{: .no_toc }")
            lines.insert(module_heading_idx + 2, "")
            if (
                functions_heading_idx is not None
                and functions_heading_idx > module_heading_idx
            ):
                functions_heading_idx += 2

    if module_heading_idx is not None and functions_heading_idx is not None:
        del lines[module_heading_idx + 1 : functions_heading_idx]
        lines.insert(module_heading_idx + 1, "")
        functions_heading_idx = module_heading_idx + 2

    if functions_heading_idx is not None:
        replacement = [
            "### Functions",
            "{: .no_toc .text-delta }",
            "",
            "1. TOC",
            "{:toc}",
            "",
        ]
        lines[functions_heading_idx : functions_heading_idx + 1] = replacement

    cleaned = "\n".join(lines).strip() + "\n"
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def get_existing_front_matter(path: Path) -> str | None:
    if not path.exists():
        return None

    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None

    end = text.find("\n---\n", 4)
    if end == -1:
        return None

    return text[: end + 5].strip() + "\n"


def default_front_matter(title: str, nav_order: int) -> str:
    return (
        "---\n"
        f"title: {title}\n"
        "layout: page\n"
        "parent: Documentation\n"
        f"nav_order: {nav_order}\n"
        "---\n"
    )


def write_module_docs(content: str, docs_dir: Path) -> None:
    anchor_positions = {
        anchor: content.find(f'<a name="{anchor}"></a>') for anchor in MODULE_ORDER
    }
    anchor_positions = {k: v for k, v in anchor_positions.items() if v != -1}

    for anchor, target in DOC_TARGETS.items():
        block = find_anchor_block(content, anchor, anchor_positions)
        normalized = normalize_module_block(block)

        output_path = docs_dir / target["file"]
        front_matter = get_existing_front_matter(output_path)
        if front_matter is None:
            front_matter = default_front_matter(
                title=target["title"], nav_order=target["nav_order"]
            )

        final_text = f"{front_matter}\n{normalized}"
        output_path.write_text(final_text, encoding="utf-8")
        print(f"Updated {output_path}")


def main() -> None:
    args = parse_args()
    input_path = args.input_file
    docs_dir = args.docs_dir

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    docs_dir.mkdir(parents=True, exist_ok=True)

    content = input_path.read_text(encoding="utf-8")
    write_module_docs(content, docs_dir)


if __name__ == "__main__":
    main()
