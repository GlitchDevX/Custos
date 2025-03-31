<template>
  <ConfigLayout>
    <EndpointSummary path="/validate-mail" title="Mail Validation"
        summary="This endpoint is used to verify if an email is valid by using different techniques."
    />
    <USwitch
        unchecked-icon="lucide-x"
        checked-icon="lucide-check"
        label="Endpoint enabled"
        size="xl"
        class="pb-8"
        v-model="state.enabled"
    />

    <div :class="{'low-opacity': !state.enabled}">
        <FeatureToggle
            title="Format Check"
            description="Apply basic format checks to an email."
            v-model="state.formatCheck"
        />
        <FeatureToggle
            title="Disposable Check"
            description="Check the email for common disposable domains."
            v-model="state.disposableCheck"
        />

        <UFormField label="Extra Disposable Domains" size="xl" class="pt-4" :class="{'low-opacity': !state.disposableCheck}">
            <p class="muted-text">
                Comma separated list of additional domains to mark as disposable.
            </p>
            <UTextarea placeholder="gmail.com, github.com..."
                :maxrows="5" :autoresize="true" class="w-116 mt-1" />
        </UFormField>

        <FeatureToggle
            title="MX Record Check"
            description="Checks if the domain has a mail server in the MX Records."
            v-model="state.mxRecordCheck" @update:model-value="onMxRecordChange"
        />
        <FeatureToggle
            title="SMTP HELO Check"
            description="Perform a SMTP HELO check verifying the existance of the mail server."
            v-model="state.smtpHelo" @update:model-value="onSmtpHeloChange"
        />
        <UFormField label="Max Mailserver Checks" size="xl" class="pt-4" :class="{'low-opacity': !state.smtpHelo}">
            <p class="muted-text">
                Maximum amount of mail servers to perform a HELO check.
            </p>
            <UInputNumber v-model="state.maxHeloChecks" class="w-32 mt-1" :min="1" />
        </UFormField>
    </div>

    <UButton label="Save" size="lg" class="mt-8"
        @click="submitConfig" :loading="sending"/>
  </ConfigLayout>
</template>

<script lang="ts" setup>
import { SET_CONFIG_PATH } from '~/assets/ts/backendConnector';

const toast = useToast();
const state = reactive({
    enabled: true,
    formatCheck: true,
    disposableCheck: true,
    disposableDomains: [],
    mxRecordCheck: true,
    smtpHelo: true,
    maxHeloChecks: 5
});

function onMxRecordChange() {
    if (state.smtpHelo && !state.mxRecordCheck) {
        state.smtpHelo = false;
    }
}
function onSmtpHeloChange() {
    if (state.smtpHelo && !state.mxRecordCheck) {
        state.mxRecordCheck = true;
    }
}

const sending = ref(false);
async function submitConfig() {
    const body = { 'namespace': 'mail_validation', 'content': state };
    sending.value = true;
    
    let result: { code: string };
    try {
        result = await $fetch<{code: string}>(SET_CONFIG_PATH, { method: 'POST', body: body, ignoreResponseError: true });
    }
    catch {
        result = {code: "FAILED"};
    }

    if (result?.code === "OK") {
        showSuccess();
    }
    else {
        showFail();
    }
    sending.value = false;
}

function showSuccess() {
    toast.add({
        title: 'Success',
        description: 'Updated config in the backend.',
        icon: 'lucide-check',
        color: 'success'
    });
}
function showFail() {
    toast.add({
        title: 'Failed',
        description: 'Failed to update config in the backend.',
        icon: 'lucide-x',
        color: 'error',
        duration: 8000,
        actions: [
            {
                icon: 'lucide-refresh-cw',
                label: 'retry',
                variant: 'outline',
                color: 'neutral',
                onClick: () => {
                    submitConfig();
                }
            }
        ],
    });
}
</script>

<style scoped>

</style>