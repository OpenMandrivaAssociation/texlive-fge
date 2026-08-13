%global tl_name fge
%global tl_revision 77682
%global tl_version 1.25

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
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
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The fonts are provided as Metafont source and Adobe Type 1 (pfb) files.
A small LaTeX package (fge) is included.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from fge:
Map fge.map
TL_DROPIN_EOF
