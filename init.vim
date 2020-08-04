"source ~/.config/nvim/plugged/coc_conf.vim

" PLUGIN (using vim-plug package manager. Do :PlugInstall to install plugins)
call plug#begin()
Plug 'morhetz/gruvbox'
"Plug 'davidhalter/jedi-vim'
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
"Plug 'zchee/deoplete-jedi'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
"Plug 'jiangmiao/auto-pairs'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'scrooloose/nerdtree'
Plug 'neomake/neomake'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'preservim/nerdcommenter'
call plug#end()

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
syntax on 		            " syntax highlighting
set pastetoggle=<F2>        " switch in and out of paste mode
colorscheme gruvbox
set background=dark         " set gruvbox colorscheme to dark mode
:let g:airline_theme='wombat' " set theme of airline ribbon
let g:neomake_python_enabled_markers = ['pylint'] " set pylint as python code checker
call neomake#configure#automake('nrwi', 500)
nnoremap <C-p> :GFiles<CR>  " use GFiles for quick file navigation
set relativenumber
set noerrorbells            " disable error sound effects
set smartcase
set noswapfile
set nobackup
set undodir=~/.config/nvim/undodir
set undofile
set incsearch

let g:netrw_browse_split=2
let g:netrw_banner=0
let g:netrw_winsize=25

"AUTOCOMPLETE CONFIG
"let g:jedi#completions_enabled = 0 "use deoplete for autocompletion therefore can disable
"let g:jedi#use_splits_not_buffers = "right" "open go-to func in split, not another buffer
"let g:deoplete#enable_at_startup=1 " enable deoplete autocomplete
"autocmd InsertLeave,CompleteDone * if pumvisible() == 0 | pclose | endif " auto close autocomplete
"inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"

" TERMINAL EMULATOR CONFIG
tnoremap <Esc> <C-\><C-n>

" MAP LEADER CONFIG
"let g:mapleader=','         " sets mapleader key
let g:mapleader=' '         " sets mapleader key
nnoremap <leader>h :split<cr>
nnoremap <leader>v :vsplit<cr>
xnoremap p pgvy             " allows for pasting multiple times
nnoremap <Up> <Nop>          " disable arrow keys
nnoremap <Down> <Nop>
nnoremap <Left> <Nop>
nnoremap <Right> <Nop>
inoremap  <Up>     <Nop>
inoremap  <Down>   <Nop>
inoremap  <Left>   <Nop>
inoremap  <Right>  <Nop>

" NERD TREE
let g:NERDTreeQuitOnOpen = 1
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>u :UndotreeShow<CR>
"nnoremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
nnoremap <Leader>ps :Rg<SPACE>
map <leader>pv :NERDTreeToggle<CR>
