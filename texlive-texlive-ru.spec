# revision 23042
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-ru
Version:	20111104
Release:	2
Summary:	TeX Live manual (Russian)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-ru.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-ru.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-ru package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-ru/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-ru/live4ht.cfg
%doc %{_texmfdir}/doc/texlive/texlive-ru/tex-live.css
%doc %{_texmfdir}/doc/texlive/texlive-ru/texlive-ru.css
%doc %{_texmfdir}/doc/texlive/texlive-ru/texlive-ru.html
%doc %{_texmfdir}/doc/texlive/texlive-ru/texlive-ru.pdf
%doc %{_texmfdir}/doc/texlive/texlive-ru/texlive-ru.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
