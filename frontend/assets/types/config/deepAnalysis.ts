import type { BaseConfig } from "./baseConfig";

export interface DeepAnalysisConfig extends BaseConfig {
    threshold: number;
    labelsToExclude: string[];
}