<template>
    <ConfigLayout>
        <EndpointSummary
            path="/validate-mail" title="Mail Validation"
            summary="This endpoint is used to verify if an email is valid by using different techniques."
        />

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
                    List of additional domains to mark as disposable. You can insert a comma-separated list.
                </p>
                <UInputTags v-model="state.disposableDomains" :addOnPaste="true" class="mt-1 w-full" :spellcheck="false" />
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
            @click="submitConfig"
        />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { PropType } from 'vue';
import type { MailValidationConfig } from '~/assets/types/configs';

const emit = defineEmits<{
    submit: [config: MailValidationConfig, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object as PropType<MailValidationConfig>,
        required: true
    }
});

const state = reactive<MailValidationConfig>({
    enabled: true,
    formatCheck: true,
    disposableCheck: true,
    disposableDomains: [],
    mxRecordCheck: true,
    smtpHelo: true,
    maxHeloChecks: 5
});

onBeforeMount(() => {
    Object.assign(state, props.config);
});

//#region toggle behavior

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

//#endregion

async function submitConfig() {
    emit('submit', state, 'mail_validation');
}
</script>

<style scoped>

</style>