<template>
  <div class="px-40 py-8">
    <EndpointSummary path="/validate-mail" title="Mail Validation"
        summary="This endpoint is used to verify if an email is valid by using different techniques."
    />
    <USwitch
        unchecked-icon="lucide-x"
        checked-icon="lucide-check"
        default-value
        label="Endpoint enabled"
        size="xl"
        class="pb-8"
    />

    <div>
        <FeatureToggle
            title="Format Check"
            description="Apply basic format checks to an email."
        />
        <FeatureToggle
            title="Disposable Check"
            description="Check the email for common disposable domains."
        />
        <FeatureToggle
            title="MX Record Check"
            description="Checks if the domain has a mailserver in the MX Records."
        />
        <FeatureToggle
            title="SMTP HELO Check"
            description="Perform a SMTP HELO check verifying the existance of the mail server."
        />
    </div>
  </div>
</template>

<script lang="ts" setup>

</script>

<style scoped>

</style>