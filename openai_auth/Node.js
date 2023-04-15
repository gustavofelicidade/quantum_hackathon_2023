import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
    // organization: "YOUR_ORG_ID",
    apiKey: "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",
});
const openai = new OpenAIApi(configuration);
const response = await openai.listEngines();