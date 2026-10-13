const searchInput = document.querySelector('#entry-search');
const entryCards = [...document.querySelectorAll('[data-entry-row]')];
const noSearchResults = document.querySelector('#no-search-results');
const resultsSummary = document.querySelector('#results-summary');
const messageField = document.querySelector('#id_message');
const characterCount = document.querySelector('#character-count');

if (searchInput && entryCards.length) {
    searchInput.addEventListener('input', () => {
        const query = searchInput.value.trim().toLocaleLowerCase();
        let visibleCount = 0;

        for (const card of entryCards) {
            const matches = card.textContent.toLocaleLowerCase().includes(query);
            card.hidden = !matches;
            if (matches) {
                visibleCount += 1;
            }
        }

        if (noSearchResults) {
            noSearchResults.hidden = visibleCount > 0;
        }
        if (resultsSummary) {
            resultsSummary.textContent = query
                ? `${visibleCount} of ${entryCards.length} moments`
                : '';
        }
    });
}

if (messageField && characterCount) {
    const updateCharacterCount = () => {
        const count = messageField.value.length;
        characterCount.textContent = `${count} ${count === 1 ? 'character' : 'characters'}`;
    };

    messageField.addEventListener('input', updateCharacterCount);
    updateCharacterCount();
}
