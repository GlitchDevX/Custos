import type { BaseConfig } from "./baseConfig";

export interface MailValidationConfig extends BaseConfig {
    disposableCheck: boolean;
    disposableDomains: string[];
    formatCheck: boolean;
    maxHeloChecks: number;
    mxRecordCheck: boolean;
    smtpHelo: boolean;
}