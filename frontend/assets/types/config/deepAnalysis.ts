import type { BaseConfig } from "./baseConfig";

export interface DeepAnalysisConfig extends BaseConfig {
    enabled: boolean;
    threshold: number;
    labelsToExclude: string[];
}