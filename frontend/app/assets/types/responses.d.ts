export interface MailValidationResponse {
    code: string;
    text: string;
}

export interface AnalyzerResponse {
    labels: string[];
}

export interface ContentCheckResponse {
    flags: string[],
    censored: string
}
