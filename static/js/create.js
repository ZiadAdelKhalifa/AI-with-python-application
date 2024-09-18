async function writeArticle() {
    const continueButton=document.getElementById('continue-button');
    continueButton.setAttribute('disabled','')
    const chatDiv=document.getElementById('maqal');
    const userInput=document.getElementById('articleTitle').value;
    const systemSettings='the user will write a title ,your job is to use this title to write an article in Arabic';
    await chatgptCall(userInput,systemSettings,chatDiv);
    continueButton.removeAttribute('disabled','')
    writeKeywords();
}

async function extendArticle() {
    const continueButton=document.getElementById('continue-button');
    continueButton.setAttribute('disabled','')
    const chatDiv=document.getElementById('maqal');
    const systemSettings='the user will input an article, your job is to extend the article in arabic,only give the extention';
    const userInput=document.getElementById('articleTitle').value;
    await chatgptCall(userInput,systemSettings,chatDiv);
    continueButton.removeAttribute('disabled','')

}

async function writeKeywords() {
    const chatDiv=document.getElementById('keywords');
    const systemSettings='you must write keywords/tags based on the user input ,these keywords/tags must be in arabic ,separated by comma';
    const userInput=document.getElementById('articleTitle').value;
    await chatgptCall(userInput,systemSettings,chatDiv);
    generateImage();

}