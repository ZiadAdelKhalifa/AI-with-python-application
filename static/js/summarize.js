async function summarizeArticle() {
    const userInput=document.getElementById('toSummarize').value;
    const chatDiv=document.getElementById('summarized');
    const systemSettings='the user will input a piece of text. your jop is to write a short summary, in Arabic';
    await chatgptCall(userInput,systemSettings,chatDiv,true)
writeTitle();
}

async function writeTitle() {
    const chatDiv=document.getElementById('title');
    const userInput=document.getElementById('summarized').value.slice(0,3000);
    const systemSettings='you are given a short text,give this text a short title in Arabic';
    await chatgptCall(userInput,systemSettings,chatDiv)
    
    writeKeywords();
}

async function writeKeywords() {
    const chatDiv=document.getElementById('keywords');
    const userInput=document.getElementById('summarized').value.slice(0,3000);
    const systemSettings='you must write keywords/tags based on the user input ,these keywords/tags must be in arabic ,separated by comma';
    await chatgptCall(userInput,systemSettings,chatDiv)
    generateImage()

}


