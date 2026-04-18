document.addEventListener("DOMContentLoaded", () => {
    const convertBtn = document.getElementById("convertBtn");
    const sourceCode = document.getElementById("sourceCode");
    const targetCode = document.getElementById("targetCode");
    const targetLanguage = document.getElementById("targetLanguage");
    const copyBtn = document.getElementById("copyBtn");
    const outputBadge = document.getElementById("outputBadge");
    
    // Status Bar Elements
    const statusBar = document.getElementById("statusBar");
    const statusIcon = statusBar.querySelector(".status-icon");
    const statusText = statusBar.querySelector(".status-text");

    // Loaders
    const btnText = convertBtn.querySelector(".btn-text");
    const loader = convertBtn.querySelector(".loader");

    function setStatus(type, message) {
        statusText.innerText = message;
        if (type === 'loading') {
            statusIcon.innerText = "⚡";
            statusText.classList.add("anim-pulse");
        } else if (type === 'success') {
            statusIcon.innerText = "✅";
            statusText.classList.remove("anim-pulse");
            statusIcon.style.color = "var(--success)";
        } else if (type === 'error') {
            statusIcon.innerText = "❌";
            statusText.classList.remove("anim-pulse");
            statusIcon.style.color = "var(--accent-red)";
        } else {
            statusIcon.innerText = "✅";
            statusText.classList.remove("anim-pulse");
        }
    }

    targetLanguage.addEventListener('change', () => {
        const lang = targetLanguage.value;
        outputBadge.innerText = `Playwright ${lang === 'typescript' ? 'TS' : 'JS'}`;
    });

    convertBtn.addEventListener("click", async () => {
        const code = sourceCode.value.trim();
        if (!code) {
            setStatus('error', 'Please enter some Selenium code first.');
            return;
        }

        // Set Loading State
        convertBtn.disabled = true;
        btnText.innerText = "Generating code...";
        loader.classList.remove("hidden");
        targetCode.value = "";
        setStatus('loading', 'Consulting codellama local LLM...');

        try {
            const response = await fetch("/api/convert", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    sourceCode: code,
                    targetLanguage: targetLanguage.value
                })
            });

            const data = await response.json();

            if (data.status === "success") {
                targetCode.value = data.convertedCode;
                setStatus('success', `Saved locally at: ${data.outputDirectoryPath}`);
            } else {
                targetCode.value = `// An error occurred during conversion.\n// Error: ${data.errorDetails}`;
                setStatus('error', 'Conversion failed.');
            }

        } catch (error) {
            targetCode.value = `// Network error occurred: ${error.message}`;
            setStatus('error', 'Network communication failed.');
        } finally {
            // Restore Button State
            convertBtn.disabled = false;
            btnText.innerText = "Generate Playwright Code";
            loader.classList.add("hidden");
        }
    });

    copyBtn.addEventListener("click", () => {
        if (!targetCode.value) return;
        
        navigator.clipboard.writeText(targetCode.value).then(() => {
            const originalTitle = copyBtn.title;
            copyBtn.innerText = "✅";
            copyBtn.title = "Copied!";
            
            setTimeout(() => {
                copyBtn.innerText = "📋";
                copyBtn.title = originalTitle;
            }, 2000);
        });
    });
});
