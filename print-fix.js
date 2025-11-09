function printWorksheet(worksheetId) {
    // Add print class to body
    document.body.classList.add('printing');
    
    // Hide all sections except worksheets
    const allSections = document.querySelectorAll('.section');
    allSections.forEach(section => {
        if (section.id !== 'worksheets') {
            section.style.display = 'none';
        }
    });
    
    // Hide all tab content except the one we want to print
    const allTabs = document.querySelectorAll('.tab-content');
    allTabs.forEach(tab => {
        if (tab.id !== worksheetId) {
            tab.style.display = 'none';
        }
    });
    
    // Hide navigation elements
    const header = document.querySelector('.header');
    const nav = document.querySelector('.nav');
    const tabs = document.querySelector('.tabs');
    const progressContainer = document.querySelector('.progress-container');
    
    if (header) header.style.display = 'none';
    if (nav) nav.style.display = 'none';
    if (tabs) tabs.style.display = 'none';
    if (progressContainer) progressContainer.style.display = 'none';
    document.body.style.marginLeft = '0';
    
    // Trigger print
    setTimeout(() => {
        window.print();
        
        // Restore everything after print dialog closes
        setTimeout(() => {
            document.body.classList.remove('printing');
            allSections.forEach(section => section.style.display = '');
            allTabs.forEach(tab => tab.style.display = '');
            if (header) header.style.display = '';
            if (nav) nav.style.display = '';
            if (tabs) tabs.style.display = '';
            if (progressContainer) progressContainer.style.display = '';
            document.body.style.marginLeft = '250px';
        }, 100);
    }, 100);
}
