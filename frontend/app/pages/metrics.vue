<template>
  <div class="py-4 px-8 flex gap-4 flex-col">
    <PageTitle>Custos Metrics</PageTitle>
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
        </p>

        <CodeBlock class="mt-2" lang="yaml" :showCopy="true" content="scrape_configs:
  - job_name: 'custos'
    static_configs:
      - targets: ['localhost:3060']  # assuming your Custos instance is running on port 3060" />
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
  title: 'Monitoring Dashboard' + TITLE_SUFFIX
});
</script>

<style></style>