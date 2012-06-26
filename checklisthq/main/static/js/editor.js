editorSettings = {
    nameSpace: 'chkl',
    previewParserPath: '/preview',
    onShiftEnter: {
        keepDefault: false,
        replaceWith:'\n\n'},
    previewInWindow: 'width=800, height=600, resizable=yes, scrollbars=yes',
    previewAutoRefresh: true,
    markupSet: [
        {
            name: 'Heading 1',
            key: '1',
            openWith: '\n= ',
            placeHolder: 'Your title here...',
            closeWith: ' =\n'
        },
        {
            name: 'Heading 2',
            key: '2',
            openWith: '\n== ',
            placeHolder: 'Your title here...',
            closeWith: ' ==\n'
        },
        {
            name: 'Heading 3',
            key: '3',
            openWith: '\n=== ',
            placeHolder: 'Your title here...',
            closeWith: ' ===\n'
        },
        {
            name: 'Item',
            key: 'i',
            openWith: '\n[] ',
            placeHolder: 'Your checklist item description here...'
        },
        {
            name: 'Choice Item',
            key: 'c',
            openWith: '\n() ',
            placeHolder: 'Your choice item description here...'
        },
        {
            name: 'Text Item',
            key: 't',
            openWith: '\n[...] ',
            placeHolder: 'Your text item description here...'
        },
        {
            name: 'Paragraph',
            key: 'p',
            openWith: '\n\n',
            placeHolder: 'Your paragraph of plain text here...',
            closeWith: '\n\n'
        },
        {
            name: 'Horizontal Line',
            key: 'h',
            openWith: '\n---\n'
        },
        {
            separator: '---------------'
        },
        {
            name: 'Preview',
            call:'preview',
            className:'preview'
        }
    ]
};
