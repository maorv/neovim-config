set clipboard=unnamedplus

" Neovim-qt Guifont command
command -nargs=? Guifont call rpcnotify(0, 'Gui', 'SetFont', "<args>") | let g:Guifont="<args>"
" Set the font to DejaVu Sans Mono:h13
Guifont DejaVu Sans Mono:h13

"youcomleteme
"let g:ycm_confirm_extra_conf = 0 
"let g:ycm_global_ycm_extra_conf = "~/.vim/.ycm_extra_conf.py"
let g:ycm_global_ycm_extra_conf = "~/.config/nvim/plugged/YouCompleteMe/third_party/ycmd/cpp/ycm/.ycm_extra_conf.py"

call plug#begin('~/.config/nvim/plugged')
Plug 'kien/ctrlp.vim'
Plug 'tpope/vim-fugitive'
Plug 'bling/vim-airline'
Plug 'mileszs/ack.vim'
Plug 'altercation/vim-colors-solarized'
Plug 'NLKNguyen/papercolor-theme'
Plug 'fatih/vim-go'
Plug 'Valloric/YouCompleteMe'
Plug 'critiqjo/lldb.nvim'
Plug 'rdnetto/YCM-Generator', { 'branch': 'stable'}
Plug 'equalsraf/neovim-gui-shim'
call plug#end()

"colorscheme blackboard 
set guifont=Monospace\ 14
set background=dark
colorscheme  PaperColor

" config the vim module CtrlP:
let g:ctrlp_custom_ignore = {
  \ 'dir':  '\v[\/](\.git|build|build_unittest|logs.whiteboxtest)$',
  \ 'file': '\v\.(so|pyc|swp|exe|bat|jar|zip|bz2|tar|sqlite)$',
  \ }
" Set no max file limit
let g:ctrlp_max_files = 0
" " Search from current directory instead of project root
let g:ctrlp_working_path_mode = 0

"Override indentation rules for C/C++ files
let g:c_syntax_for_h = 1
au FileType cpp setl tabstop=4
au FileType cpp setl shiftwidth=4
au FileType cpp setl expandtab
au FileType c setl tabstop=8
au FileType c setl shiftwidth=8
"au FileType c setl expandtab

map <F6> :Colin<CR>
"Fast movement in the location list:
map <C-j> :cn<CR>
map <C-k> :cp<CR>

"Fast movement in the buffer list:
map <C-h> :bp<CR>
map <C-l> :bn<CR>
map <M-Right> :bn^M
map <M-Left> :bp^M

"Fast movement for next/previous tags
map #8 :tp^M
map #9 :tn^M

"Fast movement between splits
map <M-Down> ^W^W
map <M-Up> ^WW

command! Ctags !ctags --exclude=build --exclude=build_unittest --exclude=tools -R .
command! NewFile %!python ~/.config/nvim/newfile.py %

