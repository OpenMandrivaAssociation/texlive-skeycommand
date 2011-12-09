# revision 24652
# category Package
# catalog-ctan /macros/latex/contrib/skeycommand
# catalog-date 2011-11-20 11:43:03 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-skeycommand
Version:	0.4
Release:	1
Summary:	Create commands using parameters and keyval in parallel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/skeycommand
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides tools for defining LaTeX commands and
environments using combinations of parameters and keys. All the
facilities of the ltxkeys and skeyval packages are available to
the user of skeycommand.

%pre
    %{_sbindir}/texlive.post

%post
    %{_sbindir}/texlive.post

%preun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
