<template>
  <div class="p-4 flex gap-4 flex-col">
    <Spinner v-if="loading" label="Loading Metrics"/>
    <div
      v-for="(metrics, namespace_index) in metricNamespaces"
      :key="'monitoring_metric_namespace' + namespace_index"
      class="flex flex-wrap gap-4 justify-center px-8">
      <USeparator :label="metrics[0]?.namespace" size="xl" />
      <MetricsBigNumber
        v-for="(metric, metric_index) in metrics" :key="metric.id"
        :title="metric.name" :number="metric.value"
        :animation-delay="getAnimationDelay(metric_index, namespace_index)"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';
import { METRIC_PATH } from '~/assets/ts/backendConnector';
import type { EnhancedMetric, Metric, MetricsResponse } from '~/assets/types/monitoring';

const metricNamespaces = ref<EnhancedMetric[][]>([]);

onMounted(() => {
  loadConfig();
})

const loading = ref(true);
async function loadConfig() {
  loading.value = true;
  try {
    const result = await $fetch<MetricsResponse>(METRIC_PATH, { method: 'GET' });
    metricNamespaces.value = mapMetrics(result.metrics);
    loading.value = false;
  } catch { /* empty */ }
}

function mapMetrics(metrics: Metric[]): EnhancedMetric[][] {
  const namespaces = [] as string[]; 
  const orderedMetrics = [] as EnhancedMetric[][]

  metrics.forEach(m => {
    const seperator_index = m.metric_name.indexOf('_');
    const namespace = m.metric_name.substring(0, seperator_index);
    const name = m.metric_name.substring(seperator_index + 1);

    if (!namespaces.includes(namespace)) {
      namespaces.push(namespace);
      orderedMetrics.push([]);
    }

    orderedMetrics[namespaces.indexOf(namespace)]?.push({
      namespace: namespace,
      name: name.toLowerCase().replaceAll('_', ' ').replace(/(^\w|\s\w)/g, m => m.toUpperCase()),
      id: m.metric_name,
      value: m.data
    } as EnhancedMetric)
  });
  
  return orderedMetrics;
}

function getAnimationDelay(metric_index: number, namespace_index: number) {
  const currentNamespace = metric_index / 2;
  if (namespace_index == 0) {
    return currentNamespace;
  }

  let delay = currentNamespace;
  const namespacesBefore = metricNamespaces.value.slice(0, namespace_index);
  
  namespacesBefore.forEach(n => {
    delay += n.length / 2;
  })
  
  return delay;
}

useHead({
  title: 'Monitoring Dashboard' + TITLE_SUFFIX
})
</script>

<style>

</style>