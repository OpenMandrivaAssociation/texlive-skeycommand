%global tl_name skeycommand
%global tl_revision 24652

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Create commands using parameters and keyval in parallel
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/skeycommand
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/skeycommand.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides tools for defining LaTeX commands and environments
using combinations of parameters and keys. All the facilities of the
ltxkeys and skeyval packages are available to the user of skeycommand.

