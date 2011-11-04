# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/misc/placeins.tex
# catalog-date 2009-11-10 09:15:37 +0100
# catalog-license pd
# catalog-version 2.0
Name:		texlive-placeins-plain
Version:	2.0
Release:	1
Summary:	Insertions that keep their place
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/misc/placeins.tex
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/placeins-plain.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
This TeX file provides various mechanisms (for plain TeX and
close relatives) to let insertions (footnotes, topins, pageins,
etc.) float within their appropriate section, but to prevent
them from intruding into the following section, even when
sections do not normally begin a new page. (If your sections
normally begin a new page, just use \supereject to flush out
insertions.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/placeins-plain/placeins.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
