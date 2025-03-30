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
                :maxrows="5" :autoresize="true" class="w-96 mt-1" />
        </UFormField>

        <FeatureToggle
            title="MX Record Check"
            description="Checks if the domain has a mail server in the MX Records."
            v-model="state.mxRecordCheck" @update:model-value="onMxRecordChange"
        />
        <FeatureToggle
            title="SMTP HELO Check"
            description="Perform a SMTP HELO check verifying the existance of the mail server."
            v-model="state.smtpHeloCheck" @update:model-value="onSmtpHeloChange"
        />
        <UFormField label="Max Mailserver Checks" size="xl" class="pt-4" :class="{'low-opacity': !state.smtpHeloCheck}">
            <p class="muted-text">
                Maximum amount of mail servers to perform a HELO check.
            </p>
            <UInputNumber v-model="state.maxHeloChecks" class="w-32 mt-1"/>
        </UFormField>
    </div>
  </ConfigLayout>
</template>

<script lang="ts" setup>
const state = reactive({
    enabled: true,
    formatCheck: true,
    disposableCheck: true,
    extraDisposableDomains: [],
    mxRecordCheck: true,
    smtpHeloCheck: true,
    maxHeloChecks: 5
});

function onMxRecordChange() {
    if (state.smtpHeloCheck && !state.mxRecordCheck) {
        state.smtpHeloCheck = false;
    }
}
function onSmtpHeloChange() {
    if (state.smtpHeloCheck && !state.mxRecordCheck) {
        state.mxRecordCheck = true;
    }
}
</script>

<style scoped>

</style>