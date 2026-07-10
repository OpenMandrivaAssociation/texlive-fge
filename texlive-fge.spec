%global tl_name fge
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.25
Release:	%{tl_revision}.1
Summary:	A font for Freges Grundgesetze der Arithmetik
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/fge
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fge.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are provided as Metafont source and Adobe Type 1 (pfb) files.
A small LaTeX package (fge) is included.

