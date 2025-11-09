function searchQuickStart() {
    const searchTerm = document.getElementById('quickStartSearch').value.toLowerCase();
    const content = document.getElementById('quickStartContent');
    const resultsText = document.getElementById('searchResults');
    
    if (!searchTerm) {
        // Show all content if search is empty
        const allElements = content.querySelectorAll('[data-searchable]');
        allElements.forEach(el => {
            el.style.display = '';
            // Remove highlights
            el.innerHTML = el.innerHTML.replace(/<mark class="search-highlight">(.*?)<\/mark>/gi, '$1');
        });
        resultsText.textContent = '';
        return;
    }
    
    let matchCount = 0;
    const allElements = content.querySelectorAll('[data-searchable]');
    
    allElements.forEach(el => {
        const text = el.textContent.toLowerCase();
        const originalHTML = el.getAttribute('data-original-html') || el.innerHTML;
        
        if (!el.hasAttribute('data-original-html')) {
            el.setAttribute('data-original-html', el.innerHTML);
        }
        
        if (text.includes(searchTerm)) {
            el.style.display = '';
            matchCount++;
            
            // Highlight matching text
            const regex = new RegExp(`(${searchTerm})`, 'gi');
            el.innerHTML = originalHTML.replace(regex, '<mark class="search-highlight">$1</mark>');
        } else {
            el.style.display = 'none';
        }
    });
    
    resultsText.textContent = matchCount > 0 
        ? `Found ${matchCount} section${matchCount !== 1 ? 's' : ''} matching "${searchTerm}"`
        : `No results found for "${searchTerm}"`;
}

function clearQuickStartSearch() {
    document.getElementById('quickStartSearch').value = '';
    searchQuickStart();
}
