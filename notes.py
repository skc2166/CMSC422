# for mean, do
sum([1 if (pre > 0) == (exp > 0) else 0 for pre, exp in zip(h.predictAll(datasets.TennisData.X), datasets.TennisData.Y)]) / len(datasets.TennisData.X)