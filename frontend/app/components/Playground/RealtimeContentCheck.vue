<template>
  <div class="px-4 pb-4">
    <EndpointSummary
      path="/check-content" title="Realtime Content Check"
      summary="This endpoint is used to censor and flag user content in real time." />

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
import type { ContentCheckResponse } from '~/assets/types/responses';

const backend = useBackend();

const state = reactive({
  loading: false,
  showResponse: false,
  content: "",
  response: {
    flags: [] as string[],
    censored: ""
  } satisfies ContentCheckResponse
});

async function submitRequest() {
  state.loading = true;
  state.showResponse = false;

  state.response = await backend.checkContent(state.content);  
  
  state.loading = false;
  state.showResponse = true;
}
</script>

<style>

</style>