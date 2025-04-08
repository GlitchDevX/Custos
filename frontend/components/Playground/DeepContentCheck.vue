<template>
  <div class="px-4 pb-4">
    <EndpointSummary
      path="scheduled pipeline" title="Deep Content Check"
      summary="This pipeline runs scheduled to flag user content with a deep understanding." />

    <UCard>
      <div class="flex flex-row justify-between">
        <UForm :state="{}" @submit="(_) => submitRequest()">
          <UFormField label="Content">
            <UTextarea v-model="content" class="min-w-lg" />
          </UFormField>
          <UButton label="Submit" class="mt-4" type="submit" :loading="loading" />
        </UForm>

        <UCollapsible v-model:open="showResponse" :arrow="true">
          <UButton
            block label="Show Response" variant="ghost" icon="lucide-chevron-down"
            :ui="{ leadingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200' }" />
          <template #content>
            <CodeBlock :content="JSON.stringify(response, null, 4)" language="json" />
          </template>
        </UCollapsible>
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import { PIPELINE_PATH } from '~/assets/ts/backendConnector';
const showResponse = ref(false);

const response = ref({
  code: "",
  text: ""
});
const content = ref("");
const loading = ref(false);

async function submitRequest() {
  loading.value = true;
  showResponse.value = false;
  const result = await $fetch<object>(PIPELINE_PATH, {
    method: 'POST',
    body: {'content': content.value},
    ignoreResponseError: true
  });
  
  loading.value = false;
  response.value = result as any;
  showResponse.value = true;
}
</script>

<style>

</style>