<template>
  <div class="px-4 pb-4">
    <EndpointSummary
      path="/validate-mail" title="Validate Mail"
      summary="This endpoint is used to verify if an email is valid by using different techniques." />

    <UCard>
      <div class="flex flex-row justify-between">
        <UForm :state="{}" @submit="() => submitRequest()">
          <UFormField label="Email">
            <UInput v-model="state.email" placeholder="example@gmail.com" />
          </UFormField>
          <UButton label="Submit" class="mt-4" type="submit" :loading="state.loading" />
        </UForm>

        <CollapsibleCodeBlock v-model="state.showResponse" :content="state.response" />
      </div>
    </UCard>
  </div>
</template>

<script lang="ts" setup>
import type { MailValidationResponse } from '~/assets/types/responses';

const backend = useBackend();

const state = reactive({
  loading: false,
  showResponse: false,
  email: "",
  response: {
    code: "",
    text: ""
  } satisfies MailValidationResponse
});

async function submitRequest() {
  state.loading = true;
  state.showResponse = false;

  state.response = await backend.validateMail(state.email);
  
  state.loading = false;
  state.showResponse = true;
}
</script>

<style>

</style>