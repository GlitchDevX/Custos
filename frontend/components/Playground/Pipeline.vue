<template>
    <div class="px-4 pb-4">
      <EndpointSummary
        path="/pipeline" title="Pipeline"
        summary="This endpoint is used to submit content to the pipeline and trigger it." />
  
    <UCard class="mt-4">
        <div class="flex flex-row justify-between">
          <UForm :state="{}" @submit="() => submitReport()">
            <UFormField label="User Id">
              <UInput v-model="reportContent.userId" class="min-w-lg" />
            </UFormField>
            <UFormField label="Content" class="mt-2">
              <UTextarea v-model="reportContent.content" class="min-w-lg" />
            </UFormField>
            <div class="flex flex-row gap-2 mt-4">
              <UButton label="Report Content" type="submit" :loading="reportLoading" />
              <UButton label="Trigger Pipeline" :loading="triggerLoading" variant="subtle" @click="triggerPipeline()" />
            </div>
          </UForm>

          <UCollapsible v-model:open="showResponse" :arrow="true" class="group">
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
import { PIPELINE_PATH, REPORT_CONTENT_PATH } from '~/assets/ts/backendConnector';

const response = ref({ 
  code: "",
  text: ""
});

const reportContent = reactive({
  userId: "testUserId",
  content: "",
});

const reportLoading = ref(false);
const showResponse = ref(false);
async function submitReport() {
  reportLoading.value = true;
  showResponse.value = false;

  const result = await $fetch<object>(REPORT_CONTENT_PATH, {
    method: 'POST',
    body: {'content': reportContent.content, "userId": reportContent.userId},
    ignoreResponseError: true
  });

  reportLoading.value = false;
  response.value = result as any;
  showResponse.value = true;
}

const triggerLoading = ref(false);
async function triggerPipeline() {
    triggerLoading.value = true;
    showResponse.value = false;
    const result = await $fetch<object>(PIPELINE_PATH, {
        method: 'PUT',
        ignoreResponseError: true
    });
    
    triggerLoading.value = false;
    response.value = result as any;
    showResponse.value = true;
}
</script>

<style>

</style>