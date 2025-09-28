<template>
  <div class="py-4 px-8 flex gap-4 flex-col">
    <PageTitle>Custos Service Metrics</PageTitle>
    <p>
      Custos offers a prometheus exporter on the path
      <UBadge label="/metrics" variant="subtle" /> that you can scrape with your Prometheus instance.
    </p>

    <UCard>
      <template #header>
        <h2 class="text-2xl font-bold">
          Prometheus Scraper Config
        </h2>
        <p>
          Edit your prometheus config at
          <UBadge label="/etc/prometheus/prometheus.yml" color="neutral" variant="subtle" />
          and add this scrape config:
        </p>

        <CodeBlock class="mt-2" lang="yaml" :showCopy="true" :content="prometheusConfig" />
      </template>
      <template #default>
        <h2 class="text-2xl font-bold">
          Grafana Dashboard
        </h2>
        <p>
          Create a new grafana dashboard from this json.
        </p>
        <CodeBlock class="mt-2 h-64" lang="json" :showCopy="true" :content="grafanaDashboard" />
      </template>
    </UCard>

    <h2 class="text-2xl font-bold">
      Current Output
    </h2>
    <CodeBlock :content="metrics">
      <Spinner v-if="loading" label="Loading Metrics" />
    </CodeBlock>
  </div>
</template>

<script lang="ts" setup>
import { TITLE_SUFFIX } from '~/assets/data/appData';
import grafanaDashboard from '~/assets/data/metric-configs/grafana-dashboard.json?raw';
import prometheusConfig from '~/assets/data/metric-configs/prometheus-config.yml?raw';

const { getMetrics } = useBackend();

const metrics = ref("");
const loading = ref(true);

onMounted(() => {
  loadMetrics();
})

async function loadMetrics() {
  loading.value = true;
  try {
    metrics.value = await getMetrics();
    loading.value = false;
  } catch { /* empty */ }
}

useHead({
  title: 'Metrics' + TITLE_SUFFIX
});
</script>

<style></style>