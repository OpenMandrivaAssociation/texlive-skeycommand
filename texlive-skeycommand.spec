# revision 24652
# category Package
# catalog-ctan /macros/latex/contrib/skeycommand
# catalog-date 2011-11-20 11:43:03 +0100
# catalog-license lppl1.3
# catalog-version 0.4
Name:		texlive-skeycommand
Version:	0.4
Release:	6
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 756065
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 739877
- texlive-skeycommand

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 719547
- texlive-skeycommand
- texlive-skeycommand
- texlive-skeycommand
- texlive-skeycommand

