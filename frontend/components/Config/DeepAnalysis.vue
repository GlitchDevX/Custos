<template>
    <ConfigLayout>
        <EndpointSummary
path="/analysis" title="Deep Content Analysis"
            summary="This endpoint is used to analyze user content utilizing a neuronal network." />
        <div>
            <USwitch
v-model="state.enabled" unchecked-icon="lucide-x" checked-icon="lucide-check"
                label="Endpoint enabled" size="xl" class="pb-8" />

            <div :class="{ 'low-opacity': !state.enabled }">
                <UFormField label="Model Threshold" size="xl">
                    <p class="muted-text">
                        Defines the value at which a label is counted. The lower the value, the more sensitive it is.
                    </p>
                    <div class="flex gap-2 justify-center items-center mt-2">
                        <UInputNumber
v-model="state.threshold" :step="0.1" :min="0.5" :max="1" class="w-24"
                            :ui="{ increment: 'hidden', decrement: 'hidden', base: 'px-2' }" />
                        <USlider v-model="state.threshold" :step="0.01" :min="0.5" :max="1" />
                    </div>
                </UFormField>

                <UFormField label="Exclude Labels" size="xl" class="pt-8">
                    <p class="muted-text">
                        Which labels to not report.
                    </p>
                    <div class="flex gap-2 h-10 mt-1">
                        <UDropdownMenu :items="labels" @select="console.log('selected')">
                            <UButton label="Add" icon="lucide:plus" variant="subtle" color="neutral" />
                        </UDropdownMenu>
                        <UInputTags v-model="state.labelsToExclude" class="w-full" :ui="{ input: 'hidden' }" />
                    </div>
                </UFormField>
            </div>
        </div>
        <UButton label="Save" size="lg" class="mt-8" @click="submitConfig" />
    </ConfigLayout>
</template>

<script lang="ts" setup>
import type { DropdownMenuItem } from '@nuxt/ui';
import type { DeepAnalysisConfig } from '~/assets/types/config/deepAnalysis';

const emit = defineEmits<{
    submit: [config: DeepAnalysisConfig, namespace: string]
}>();
const props = defineProps({
    config: {
        type: Object as PropType<DeepAnalysisConfig>,
        required: true
    }
});

const state = reactive<DeepAnalysisConfig>({
    enabled: true,
    threshold: 0.85,
    labelsToExclude: []
});

onBeforeMount(() => {
    Object.assign(state, props.config);
});

async function submitConfig() {
    emit("submit", state, 'deep_analysis');
}

const labels = ref<DropdownMenuItem[]>(
    [
        "toxicity",
        "severe_toxicity",
        "obscene",
        "identity_attack",
        "insult",
        "threat",
        "sexual_explicit"
    ].map((label) => {
        return {
            label,
            onSelect: () => addExclusion(label)
        }
    })
);
function addExclusion(name: string) {
    if (!state.labelsToExclude.includes(name)) {
        state.labelsToExclude.push(name)
    }
}
</script>

<style scoped></style>