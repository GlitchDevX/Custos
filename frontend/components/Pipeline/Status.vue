<template>
  <UCard>
    <div class="flex gap-2 items-center">
      <h2 class="text-2xl font-bold" >
        Pipeline Status
      </h2>
      <UBadge v-if="status.active" label="Active" icon="lucide-circle-dot" color="success" />
      <UBadge v-else label="Inactive" icon="lucide-circle-dot" color="neutral" />
    </div>
    
    <UProgress v-model="status.processed" :max="status.total" class="mt-4" />
    <div class="text-xl font-bold mt-2 flex justify-between">
      <div>
        <span>{{ status.processed }}</span>
        <span class="muted-text text-lg">
          Processed
        </span>
      </div>
      <div>
        <span>{{ status.total }}</span>
        <span class="muted-text text-lg">
          Total
        </span>
      </div>
    </div>

    <div class="flex justify-between items-end">
      <p class="dimmed-text mt-4">
        Last execution: {{ status.lastExecution }}
      </p>
      <UButton icon="lucide-refresh-cw" variant="ghost" :loading="loading" color="neutral" @click="loadStatus" />
    </div>
  </UCard>
</template>

<script lang="ts" setup>
import { PIPELINE_PATH } from '~/assets/ts/backendConnector';

const status = reactive({
	active: false,
	total: 0,
	processed: 0,
	lastExecution: "n/a"
});

onMounted(() => {
  loadStatusRec();
})

const loading = ref(true);
async function loadStatus() {
  loading.value = true;
  const result = await $fetch<any>(PIPELINE_PATH);
  Object.assign(status, result);
  setTimeout(() => {
    loading.value = false
  }, 500);
}

async function loadStatusRec() {
  if (leftPage.value) {
    return;
  }
  await loadStatus();
  const timeout = status.active ? 2000 : 10000;
  setTimeout(loadStatusRec, timeout);
}

const leftPage = ref(false);
onBeforeUnmount(() => {
  leftPage.value = true;
})
</script>

<style>

</style>