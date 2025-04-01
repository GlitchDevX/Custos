export type ConfigResponse = {
    disposableCheck: boolean,
    disposableDomains: string[],
    enabled: boolean,
    formatCheck: boolean,
    maxHeloChecks: number,
    mxRecordCheck: boolean,
    smtpHelo: boolean
}

export type ConfigBody = {
    disposableCheck: boolean,
    disposableDomains: string[] | string,
    enabled: boolean,
    formatCheck: boolean,
    maxHeloChecks: number,
    mxRecordCheck: boolean,
    smtpHelo: boolean
}