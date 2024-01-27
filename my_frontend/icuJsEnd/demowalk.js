const fs = require('fs');
const path = require('path');

function displayFolderStructure(basePath, prefix = '') {
  const entries = fs.readdirSync(basePath);

  entries.forEach((entry, index) => {
    const entryPath = path.join(basePath, entry);
    const stats = fs.statSync(entryPath);

    if (stats.isDirectory()) {
      console.log();
      displayFolderStructure(entryPath, );
    } else {
      console.log();
    }
  });
}

// Replace './docisfy-test-management' with the path to your Docisfy test management directory
displayFolderStructure('./docisfy-test-management');
