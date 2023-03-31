Name:		texlive-skeycommand
Version:	24652
Release:	2
Summary:	Create commands using parameters and keyval in parallel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skeycommand
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools for defining LaTeX commands and
environments using combinations of parameters and keys. All the
facilities of the ltxkeys and skeyval packages are available to
the user of skeycommand.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/skeycommand/skeycommand.sty
%doc %{_texmfdistdir}/doc/latex/skeycommand/README
%doc %{_texmfdistdir}/doc/latex/skeycommand/skeycommand-guide.cfg
%doc %{_texmfdistdir}/doc/latex/skeycommand/skeycommand-guide.pdf
%doc %{_texmfdistdir}/doc/latex/skeycommand/skeycommand-guide.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
