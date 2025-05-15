---
title: Documentation
layout: page
nav_order: 3
---

# Documentation
{: no_toc }

This page presents the different modules attached to the `oscfar` package. Some functions are quite useful and have also been given some aliases to access them faster. You can also access a list of parameters that have worked well so far on tested datasets:

```python
best_params = {
    "guard_cells": 1,
    "train_cells": 8,
    "rank_k": 0.75,
    "threshold_factor": 0.9,
    "averaging": 2,
    "min_snr": 2,
    "baseline": 0.15,
}
```

This can be used like a `**kwargs` parameter for the OS-CFAR algorithms. Note that the minimum distance argument needs to be provided each time the algorithms are used.

## General use methods

| Alias                                                                                                                   | Full link to function                         |
| :---------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| [`oscfar.os_cfar`](https://chujo58.github.io/oscfar/docs/oscfar-cfar.html#%F0%9F%85%B5-oscfarcfaros_cfar_1d)            | `oscfar.cfar.os_cfar_1d`                      |
| [`vwindow_os_cfar`](https://chujo58.github.io/oscfar/docs/oscfar-cfar.html#%F0%9F%85%B5-oscfarcfarvariable_window_cfar) | `oscfar.cfar.variable_window_os_cfar_indices` |

## Filters

| Alias                                                                                                                               | Full link to function                      |
| :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| [`baseline_filter`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersremove_baseline_peaks)      | `oscfar.filters.remove_baseline_peaks`     |
| [`lowpass_filter`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfilterslowpass_filter)              | `oscfar.filters.lowpass_filter`            |
| [`highpass_filter`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltershighpass_filter)            | `oscfar.filters.highpass_filter`           |
| [`median_smoothing`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersmedian_filter)             | `oscfar.filters.median_filter`             |
| [`mean_smoothing`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersmoving_average_filter)       | `oscfar.filters.moving_average_filter`     |
| [`group_peaks`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersfind_representative_peaks)      | `oscfar.filters.find_representative_peaks` |
| [`force_min_dist`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersenforce_min_distance)        | `oscfar.filters.enforce_min_distance`      |
| [`check_snr`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersverify_peaks_snr)                 | `oscfar.filters.verify_peaks_snr`          |
| [`force_max_extent`](https://chujo58.github.io/oscfar/docs/oscfar-filters.html#%F0%9F%85%B5-oscfarfiltersfilter_peaks_by_extent_1d) | `oscfar.filters.filter_peaks_by_extent_1d` |

## Gaussian functions

| Alias                                                                                                                                                  | Full link to function                              |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------- |
| [`multi_gaussian`](https://chujo58.github.io/oscfar/docs/oscfar-gaussian_fit.html#%F0%9F%85%B5-oscfargaussian_fitsum_of_gaussians)                     | `oscfar.gaussian_fit.sum_of_gaussians`             |
| [`multi_scattered_gaussian`](https://chujo58.github.io/oscfar/docs/oscfar-gaussian_fit.html#%F0%9F%85%B5-oscfargaussian_fitsum_of_scattered_gaussians) | `oscfar.gaussian_fit.sum_of_scattered_gaussians`   |
| [`grid_search_gaussian`](https://chujo58.github.io/oscfar/docs/oscfar-gaussian_fit.html#%F0%9F%85%B5-oscfargaussian_fitfind_best_multi_gaussian_fit)   | `oscfar.gaussian_fit.find_best_multi_gaussian_fit` |

## Utilities

| Alias                                                                                                              | Full link to function        |
| :----------------------------------------------------------------------------------------------------------------- | :--------------------------- |
| [`peaks`](https://chujo58.github.io/oscfar/docs/oscfar-utils.html#%F0%9F%85%B5-oscfarutilspeaks)                   | `oscfar.utils.Peaks`         |
| [`waterfall_axes`](https://chujo58.github.io/oscfar/docs/oscfar-utils.html#%F0%9F%85%B5-oscfarutilswaterfall_axes) | `oscfar.utils.WaterFallAxes` |
| [`waterfall_grid`](https://chujo58.github.io/oscfar/docs/oscfar-utils.html#%F0%9F%85%B5-oscfarutilswaterfall_grid) | `oscfar.utils.WaterFallGrid` |
| [`npz_reader`](https://chujo58.github.io/oscfar/docs/oscfar-utils.html#%F0%9F%85%B5-oscfarutilsnpz_reader)         | `oscfar.utils.npz_reader`    |
| [`npz_writer`](https://chujo58.github.io/oscfar/docs/oscfar-utils.html#%F0%9F%85%B5-oscfarutilsnpz_writer)         | `oscfar.utils.npz_writer`    |
