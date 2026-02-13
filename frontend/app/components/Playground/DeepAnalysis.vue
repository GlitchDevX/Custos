<template>
  <div class="px-4 pb-4">
    <EndpointSummary
      path="/analysis" title="Deep Content Analysis"
      summary="This endpoint is used to analyze user content utilizing a neuronal network." />

    <UCard>
      <div class="flex flex-row justify-between">
        <UForm :state="{}" @submit="() => submitRequest()">
          <UFormField label="Content">
            <UTextarea v-model="state.content" class="min-w-lg" />
          </UFormField>
          <UButton label="Submit" class="mt-4" type="submit" :loading="state.loading" />
        </UForm>

        <CollapsibleCodeBlock v-model="state.showResponse" :content="state.response" />
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import type { AnalyzerResponse } from '~/assets/types/responses';

const backend = useBackend();

const state = reactive({
  loading: false,
  showResponse: false,
  content: "",
  response: {
    labels: [] as string[],
  } satisfies AnalyzerResponse
});


async function submitRequest() {
  state.loading = true;
  state.showResponse = false;

  state.response = await backend.executeAnalysis(state.content);
  
  state.loading = false;
  state.showResponse = true;
}
</script>

<style>

</style>