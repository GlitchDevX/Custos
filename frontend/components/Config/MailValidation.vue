<template>
  <ConfigLayout>
    <EndpointSummary
        path="/validate-mail" title="Mail Validation"
        summary="This endpoint is used to verify if an email is valid by using different techniques."
    />
    <Spinner v-if="loading" label="Loading Config"/>
    <UAlert
        v-if="loadingFailed"
        color="error" title="Failed to load Config"
        icon="lucide-triangle-alert"
        :actions="[retryButton]" />
    <div v-show="loaded">
        <USwitch
            v-model="state.enabled"
            unchecked-icon="lucide-x"
            checked-icon="lucide-check"
            label="Endpoint enabled"
            size="xl"
            class="pb-8"
        />

        <div :class="{'low-opacity': !state.enabled}">
            <FeatureToggle
                v-model="state.formatCheck"
                title="Format Check"
                description="Apply basic format checks to an email."
            />
            <FeatureToggle
                v-model="state.disposableCheck"
                title="Disposable Check"
                description="Check the email for common disposable domains."
            />

            <UFormField label="Extra Disposable Domains" size="xl" class="pt-4" :class="{'low-opacity': !state.disposableCheck}">
                <p class="muted-text">
                    Comma separated list of additional domains to mark as disposable.
                </p>
                <UTextarea
                    v-model="state.disposableDomains" spellcheck="false"
                    placeholder="gmail.com, github.com..."
                    :maxrows="5" :autoresize="true" class="w-116 mt-1" />
            </UFormField>

            <FeatureToggle
                v-model="state.mxRecordCheck"
                title="MX Record Check"
                description="Checks if the domain has a mail server in the MX Records."
                @update:model-value="onMxRecordChange"
            />
            <FeatureToggle
                v-model="state.smtpHelo"
                title="SMTP HELO Check"
                description="Perform a SMTP HELO check verifying the existance of the mail server."
                @update:model-value="onSmtpHeloChange"
            />
            <UFormField label="Max Mailserver Checks" size="xl" class="pt-4" :class="{'low-opacity': !state.smtpHelo}">
                <p class="muted-text">
                    Maximum amount of mail servers to perform a HELO check.
                </p>
                <UInputNumber v-model="state.maxHeloChecks" class="w-32 mt-1" :min="1" />
            </UFormField>
        </div>

        <UButton
            label="Save" size="lg" class="mt-8"
            :loading="sending"
            @click="submitConfig"
        />
    </div>
</ConfigLayout>
</template>

<script lang="ts" setup>
import type { ButtonProps } from '@nuxt/ui';
import { CONFIG_PATH } from '~/assets/ts/backendConnector';
import type { ConfigBody, ConfigResponse } from '~/assets/types/mailValidation';

const toast = useToast();
const state = reactive({
    enabled: true,
    formatCheck: true,
    disposableCheck: true,
    disposableDomains: "",
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


const loading = ref(true);
const loaded = ref(false);
const loadingFailed = ref(false);
async function loadConfig() {
    let result: ConfigResponse | undefined;
    loading.value = true;
    loaded.value = false;
    loadingFailed.value = false;
    try {
        result = await $fetch<ConfigResponse>(CONFIG_PATH + "?namespace=mail_validation", { method: 'GET' });
        Object.assign(state, result);
        state.disposableDomains = result.disposableDomains.join(', ');
        loaded.value = true;
        
    } catch {
        loadingFailed.value = true
    }

    if (result === undefined) {
        showFail("Failed to get config from the backend", loadConfig);
    }

    loading.value = false;
}
loadConfig();
const sending = ref(false);
async function submitConfig() {
    const bodyState = { ...state } as ConfigBody;
    bodyState.disposableDomains = state.disposableDomains.split(', ').map(s => s.trim());

    const body = { 'namespace': 'mail_validation', 'content': bodyState };
    sending.value = true;
    
    let result: { code: string };
    try {
        result = await $fetch<{code: string}>(CONFIG_PATH, { method: 'POST', body: body, ignoreResponseError: true });
    }
    catch {
        result = {code: "FAILED"};
    }

    if (result?.code === "OK") {
        showSuccess();
    }
    else {
        showFail("Failed to update config in the backend.", submitConfig);
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
function showFail(description: string, retryCallback: () => void) {
    toast.add({
        title: 'Failed',
        description: description,
        icon: 'lucide-x',
        color: 'error',
        duration: 8000,
        actions: [
            {
                icon: 'lucide-refresh-cw',
                label: 'retry',
                variant: 'outline',
                color: 'neutral',
                onClick: retryCallback
            }
        ],
    });
}

const retryButton = {
    icon: 'lucide-refresh-cw',
    label: 'retry',
    variant: 'soft',
    color: 'neutral',
    onClick: loadConfig
} as ButtonProps
</script>

<style scoped>

</style>