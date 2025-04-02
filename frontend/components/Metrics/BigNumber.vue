<template>
  <div>
  <UCard v-for="metric in metrics" :key="metric.metric_name">
    <span>{{ metric.metric_name }}</span>
    <span class="text-5xl font-bold">{{ metric.data }}</span>
  </UCard>
  </div>
</template>

<script lang="ts" setup>
import { METRIC_PATH } from '~/assets/ts/backendConnector';

    const props = defineProps({zahl: Number});
    const metrics = ref([]);
    onMounted(() => {
        loadConfig();
    })

    async function loadConfig() {
        let result: object | undefined;
        try {
            result = await $fetch<object>(METRIC_PATH, { method: 'GET' });
            metrics.value = result.metric;
            console.log(result);
            
        } catch {
        }
    }

</script>

<style>

</style>