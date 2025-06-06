from evidently.legacy.metrics.recsys.base_top_k import TopKMetric
from evidently.legacy.metrics.recsys.base_top_k import TopKMetricRenderer
from evidently.legacy.renderers.base_renderer import default_renderer


class PrecisionTopKMetric(TopKMetric):
    class Config:
        type_alias = "evidently:metric:PrecisionTopKMetric"

    def key(self):
        return "precision"


@default_renderer(wrap_type=PrecisionTopKMetric)
class PrecisionTopKMetricRenderer(TopKMetricRenderer):
    yaxis_name = "precision@k"
    header = "Precision"
