<template>
    <ConfigLayout>
        <EndpointSummary
            path="scheduled pipeline" title="Pipeline Check"
            summary="This deep content check pipeline runs on a scheduled base to flag user content with a deep understanding."
        />
        <USwitch
            v-model="state.enabled"
            unchecked-icon="lucide-x"
            checked-icon="lucide-check"
            label="Endpoint enabled"
            size="xl" class="pb-8"
        />

        <div :class="{'low-opacity': !state.enabled}">
            <FeatureToggle
                v-model="state.scheduledExecution"
                title="Scheduled Execution"
                description="Execute the pipeline on a scheduled base."
            />

            <UFormField
                label="Execution Interval"
                size="xl" class="pt-8"
                :class="{'low-opacity': !state.scheduledExecution}"
            >
                <p class="muted-text">
                    Amount of hours between the execution of the pipeline.
                </p>
                <UInputNumber
                    v-model="state.executionIntervalHours"
                    size="lg" :step="0.5" :min="0.5"
                    class="mt-1 w-32"
                />
            </UFormField>
        </div>
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { ConfigBody } from '~/assets/types/pipeline';

const emit = defineEmits<{
    submit: [config: object, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object,
        required: true
    }
});

const state = reactive({
    enabled: true,
    scheduledExecution: true,
    executionIntervalHours: 1,
});

onBeforeMount(() => {
    Object.assign(state, props.config);
    // state.validFlags = props.config["validFlags"].join(', ');
});

async function submitConfig() {
    const bodyState = { ...state } as ConfigBody;
    // bodyState.validFlags = state.validFlags.split(', ').map(s => s.trim()).filter(s => s.length > 0);

    emit("submit", bodyState, 'pipeline');
}
</script>

<style scoped></style>