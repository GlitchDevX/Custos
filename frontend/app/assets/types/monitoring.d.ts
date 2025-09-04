export type Metric = { metric_name: string, data: number }
export type EnhancedMetric = { namespace: string, name: string, id: string, value: number }

export type MetricsResponse = { metrics: Metric[] }
