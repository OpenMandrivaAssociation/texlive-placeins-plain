%global tl_name placeins-plain
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Insertions that keep their place
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/misc/placeins.tex
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins-plain.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This TeX file provides various mechanisms (for plain TeX and close
relatives) to let insertions (footnotes, topins, pageins, etc.) float
within their appropriate section, but to prevent them from intruding
into the following section, even when sections do not normally begin a
new page. (If your sections normally begin a new page, just use
\supereject to flush out insertions.)

