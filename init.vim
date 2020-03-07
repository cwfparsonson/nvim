" GENERAL CONFIG
set nocompatible            " disable compatibility to old-time vi
set showmatch               " show matching brackets.
set ignorecase              " case insensitive matching
set mouse=a                 " middle-click paste with mouse
set clipboard=unnamed       " enables pasting from default clipboard
set hlsearch                " highlight search results
set tabstop=4               " number of columns occupied by a tab character
set softtabstop=4           " see multiple spaces as tabstops so <BS> does the right thing
set expandtab               " converts tabs to white space
set shiftwidth=4            " width for autoindents
set autoindent              " indent a new line the same amount as the line just typed
set number                  " add line numbers
set wildmode=longest,list   " get bash-like tab completions
set cc=80                   " set an 80 column border for good coding style
filetype plugin indent on   " allows auto-indenting depending on file type
syntax on 		    " syntax highlighting
colorscheme default 	    " set colour scheme as default

" TERMINAL EMULATOR CONFIG
tnoremap <Esc> <C-\><C-n>

" MAP LEADER CONFIG
let g:mapleader=','         " sets mapleader key
nnoremap <leader>h :split<cr>
nnoremap <leader>v :vsplit<cr>

