<template>
  <div class="px-4 pb-4">
    <EndpointSummary
        path="/validate-mail"
        title="Validate Mail"
        summary="This endpoint is used to verify if an email is valid by using different techniques." />

    <UCard>
      <div class="flex flex-row justify-between">
        <div>
          <UFormField label="Email">
            <UInput v-model="email" placeholder="jonas.ringeis@gmail.com" />
          </UFormField>
          <UButton
            label="Submit" class="mt-4"
            :loading="loading"
            @click="submitRequest"
            />
        </div>
        <UCollapsible :arrow="true" default-open>
          <UButton
            block label="Show Response" variant="ghost" icon="lucide-chevron-down" class="group"
            :ui="{
              leadingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200'
            }"
          />
          <template #content>
            <CodeBlock :content="JSON.stringify(response, null, 4)"/>
          </template>
        </UCollapsible>
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import { VALIDATE_MAIL_PATH } from '~/assets/ts/backendConnector';

const response = ref({
  code: "DISPOSABLE",
  text: "Disposable Emails are not allowed"
});
const email = ref("");
const loading = ref(false);

async function submitRequest() {
  loading.value = true;
  const result = await $fetch<object>(VALIDATE_MAIL_PATH, {
    method: 'POST',
    body: {'mail': email.value}
  });
  
  loading.value = false;
  response.value = result as any;
}
</script>

<style>

</style>