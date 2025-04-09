<template>
    <div class="px-4 pb-4">
      <EndpointSummary path="/validate-mail" title="Validate Mail"
        summary="This endpoint is used to verify if an email is valid by using different techniques." />
  
    <UCard class="mt-4">
        <h3 class="text-2xl font-bold">
            Report Content
        </h3>
        <div class="flex flex-row justify-between mt-2">
          <UForm :state="{}" @submit="(_) => submitReport()">
            <UFormField label="User Id">
              <UInput v-model="reportContent.userId" class="min-w-lg" />
            </UFormField>
            <UFormField label="Content">
              <UTextarea v-model="reportContent.content" class="min-w-lg" />
            </UFormField>
            <UButton label="Submit" class="mt-4" type="submit" :loading="reportLoading" />
          </UForm>

          <UCollapsible v-model:open="showResponse" :arrow="true" class="group">
            <UButton
              block label="Show Response" variant="ghost" icon="lucide-chevron-down"
              :ui="{ leadingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200' }" />
            <template #content>
              <CodeBlock :content="JSON.stringify(reportResponse, null, 4)" language="json" />
            </template>
          </UCollapsible>
        </div>
    </UCard>
      <UCard class="mt-4">
        <h3 class="text-2xl font-bold">
            Trigger Pipeline
        </h3>
        <div class="flex flex-row justify-between mt-2">
            <div>
                <UButton label="Trigger" class="mt-4" type="submit" :loading="triggerLoading" @click="triggerPipeline()" />
            </div>
  
          <UCollapsible v-model:open="showTriggerResponse" :arrow="true" class="group">
            <UButton
              block label="Show Response" variant="ghost" leading-icon="lucide-chevron-down"
              :ui="{ leadingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200' }" />
            <template #content>
              <CodeBlock :content="JSON.stringify(triggerResponse, null, 4)" language="json" />
            </template>
          </UCollapsible>
        </div>
      </UCard>
    </div>
  </template>

<script lang="ts" setup>
import { PIPELINE_PATH, REPORT_CONTENT_PATH } from '~/assets/ts/backendConnector';
const showResponse = ref(false);

const reportResponse = ref({
    code: "",
    text: ""
});
const reportContent = reactive({
    content: "",
    userId: "",
});
const reportLoading = ref(false);
async function submitReport() {
    reportLoading.value = true;
    showResponse.value = false;
    const result = await $fetch<object>(REPORT_CONTENT_PATH, {
        method: 'POST',
        body: {'content': reportContent.content, "userId": reportContent.userId},
        ignoreResponseError: true
    });

    reportLoading.value = false;
    reportResponse.value = result as any;
    showResponse.value = true;
}

const triggerLoading = ref(false);
const showTriggerResponse = ref(false);
const triggerResponse = ref({ "code": "" });
async function triggerPipeline() {
    triggerLoading.value = true;
    showTriggerResponse.value = false;
    const result = await $fetch<object>(PIPELINE_PATH, {
        method: 'PUT',
        ignoreResponseError: true
    });
    
    triggerLoading.value = false;
    triggerResponse.value = result as any;
    showTriggerResponse.value = true;
}
</script>

<style>

</style>