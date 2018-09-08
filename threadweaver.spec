#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : threadweaver
Version  : 5.50.0
Release  : 3
URL      : https://download.kde.org/stable/frameworks/5.50/threadweaver-5.50.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.50/threadweaver-5.50.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.50/threadweaver-5.50.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: threadweaver-lib
Requires: threadweaver-license
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev qtbase-extras mesa-dev

%description
# ThreadWeaver
Helper for multithreaded programming
## Introduction
ThreadWeaver is a helper for multithreaded programming.  It uses a job-based
interface to queue tasks and execute them in an efficient way.

%package dev
Summary: dev components for the threadweaver package.
Group: Development
Requires: threadweaver-lib
Provides: threadweaver-devel

%description dev
dev components for the threadweaver package.


%package lib
Summary: lib components for the threadweaver package.
Group: Libraries
Requires: threadweaver-license

%description lib
lib components for the threadweaver package.


%package license
Summary: license components for the threadweaver package.
Group: Default

%description license
license components for the threadweaver package.


%prep
%setup -q -n threadweaver-5.50.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536438842
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536438842
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/threadweaver
cp COPYING.LIB %{buildroot}/usr/share/doc/threadweaver/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Collection
/usr/include/KF5/ThreadWeaver/ThreadWeaver/DebuggingAids
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Dependency
/usr/include/KF5/ThreadWeaver/ThreadWeaver/DependencyPolicy
/usr/include/KF5/ThreadWeaver/ThreadWeaver/DestructedState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Exception
/usr/include/KF5/ThreadWeaver/ThreadWeaver/IdDecorator
/usr/include/KF5/ThreadWeaver/ThreadWeaver/InConstructionState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Job
/usr/include/KF5/ThreadWeaver/ThreadWeaver/JobInterface
/usr/include/KF5/ThreadWeaver/ThreadWeaver/JobPointer
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Lambda
/usr/include/KF5/ThreadWeaver/ThreadWeaver/ManagedJobPointer
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QObjectDecorator
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Queue
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QueueAPI
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QueueInterface
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QueuePolicy
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QueueSignals
/usr/include/KF5/ThreadWeaver/ThreadWeaver/QueueStream
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Queueing
/usr/include/KF5/ThreadWeaver/ThreadWeaver/ResourceRestrictionPolicy
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Sequence
/usr/include/KF5/ThreadWeaver/ThreadWeaver/ShuttingDownState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/State
/usr/include/KF5/ThreadWeaver/ThreadWeaver/SuspendedState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/SuspendingState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Thread
/usr/include/KF5/ThreadWeaver/ThreadWeaver/ThreadWeaver
/usr/include/KF5/ThreadWeaver/ThreadWeaver/Weaver
/usr/include/KF5/ThreadWeaver/ThreadWeaver/WeaverImplState
/usr/include/KF5/ThreadWeaver/ThreadWeaver/WeaverInterface
/usr/include/KF5/ThreadWeaver/ThreadWeaver/WorkingHardState
/usr/include/KF5/ThreadWeaver/threadweaver/collection.h
/usr/include/KF5/ThreadWeaver/threadweaver/debuggingaids.h
/usr/include/KF5/ThreadWeaver/threadweaver/dependency.h
/usr/include/KF5/ThreadWeaver/threadweaver/dependencypolicy.h
/usr/include/KF5/ThreadWeaver/threadweaver/destructedstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/exception.h
/usr/include/KF5/ThreadWeaver/threadweaver/iddecorator.h
/usr/include/KF5/ThreadWeaver/threadweaver/inconstructionstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/job.h
/usr/include/KF5/ThreadWeaver/threadweaver/jobinterface.h
/usr/include/KF5/ThreadWeaver/threadweaver/jobpointer.h
/usr/include/KF5/ThreadWeaver/threadweaver/lambda.h
/usr/include/KF5/ThreadWeaver/threadweaver/managedjobpointer.h
/usr/include/KF5/ThreadWeaver/threadweaver/qobjectdecorator.h
/usr/include/KF5/ThreadWeaver/threadweaver/queue.h
/usr/include/KF5/ThreadWeaver/threadweaver/queueapi.h
/usr/include/KF5/ThreadWeaver/threadweaver/queueing.h
/usr/include/KF5/ThreadWeaver/threadweaver/queueinterface.h
/usr/include/KF5/ThreadWeaver/threadweaver/queuepolicy.h
/usr/include/KF5/ThreadWeaver/threadweaver/queuesignals.h
/usr/include/KF5/ThreadWeaver/threadweaver/queuestream.h
/usr/include/KF5/ThreadWeaver/threadweaver/resourcerestrictionpolicy.h
/usr/include/KF5/ThreadWeaver/threadweaver/sequence.h
/usr/include/KF5/ThreadWeaver/threadweaver/shuttingdownstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/state.h
/usr/include/KF5/ThreadWeaver/threadweaver/suspendedstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/suspendingstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/thread.h
/usr/include/KF5/ThreadWeaver/threadweaver/threadweaver.h
/usr/include/KF5/ThreadWeaver/threadweaver/threadweaver_export.h
/usr/include/KF5/ThreadWeaver/threadweaver/weaver.h
/usr/include/KF5/ThreadWeaver/threadweaver/weaverimplstate.h
/usr/include/KF5/ThreadWeaver/threadweaver/weaverinterface.h
/usr/include/KF5/ThreadWeaver/threadweaver/workinghardstate.h
/usr/include/KF5/threadweaver_version.h
/usr/lib64/cmake/KF5ThreadWeaver/KF5ThreadWeaverConfig.cmake
/usr/lib64/cmake/KF5ThreadWeaver/KF5ThreadWeaverConfigVersion.cmake
/usr/lib64/cmake/KF5ThreadWeaver/KF5ThreadWeaverTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5ThreadWeaver/KF5ThreadWeaverTargets.cmake
/usr/lib64/libKF5ThreadWeaver.so
/usr/lib64/qt5/mkspecs/modules/qt_ThreadWeaver.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5ThreadWeaver.so.5
/usr/lib64/libKF5ThreadWeaver.so.5.50.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/threadweaver/COPYING.LIB