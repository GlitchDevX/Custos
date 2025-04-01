<template>
    <ConfigLayout>
        <EndpointSummary
            path="scheduled pipeline" title="Pipeline Check"
            summary="This endpoint is used to quickly verify or censor user-content by applying rules."
        />
        <USwitch
            v-model="state.enabled"
            unchecked-icon="lucide-x"
            checked-icon="lucide-check"
            label="Endpoint enabled"
            size="xl" class="pb-8"
        />

        <div>
            <FeatureToggle
                v-model="state.check"
                title="Some Check"
                description="Placeholder description. Yoyoyo."
            />
        </div>
    </ConfigLayout>
</template>

<script lang="ts" setup>
const state = reactive({
    enabled: true,
    check: true
});
</script>

<style scoped></style>