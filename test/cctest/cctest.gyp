# Copyright 2012 the V8 project authors. All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of Google Inc. nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# The sources are kept automatically in sync with BUILD.gn.

{
  'variables': {
    'v8_code': 1,
    'generated_file': '<(SHARED_INTERMEDIATE_DIR)/resources.cc',
    'cctest_sources': [
      'compiler/c-signature.h',
      'compiler/call-tester.h',
      'compiler/codegen-tester.cc',
      'compiler/codegen-tester.h',
      'compiler/code-assembler-tester.h',
      'compiler/function-tester.cc',
      'compiler/function-tester.h',
      'compiler/graph-builder-tester.h',
      'compiler/test-basic-block-profiler.cc',
      'compiler/test-branch-combine.cc',
      'compiler/test-run-unwinding-info.cc',
      'compiler/test-gap-resolver.cc',
      'compiler/test-graph-visualizer.cc',
      'compiler/test-code-generator.cc',
      'compiler/test-code-assembler.cc',
      'compiler/test-instruction.cc',
      'compiler/test-js-context-specialization.cc',
      'compiler/test-js-constant-cache.cc',
      'compiler/test-js-typed-lowering.cc',
      'compiler/test-jump-threading.cc',
      'compiler/test-linkage.cc',
      'compiler/test-loop-analysis.cc',
      'compiler/test-machine-operator-reducer.cc',
      'compiler/test-multiple-return.cc',
      'compiler/test-node.cc',
      'compiler/test-operator.cc',
      'compiler/test-representation-change.cc',
      'compiler/test-run-bytecode-graph-builder.cc',
      'compiler/test-run-calls-to-external-references.cc',
      'compiler/test-run-deopt.cc',
      'compiler/test-run-intrinsics.cc',
      'compiler/test-run-jsbranches.cc',
      'compiler/test-run-jscalls.cc',
      'compiler/test-run-jsexceptions.cc',
      'compiler/test-run-jsobjects.cc',
      'compiler/test-run-jsops.cc',
      'compiler/test-run-load-store.cc',
      'compiler/test-run-machops.cc',
      'compiler/test-run-native-calls.cc',
      'compiler/test-run-retpoline.cc',
      'compiler/test-run-stackcheck.cc',
      'compiler/test-run-stubs.cc',
      'compiler/test-run-tail-calls.cc',
      'compiler/test-run-variables.cc',
      'compiler/test-run-wasm-machops.cc',
      'compiler/value-helper.cc',
      'compiler/value-helper.h',
      'cctest.cc',
      'cctest.h',
      'expression-type-collector-macros.h',
      'gay-fixed.cc',
      'gay-fixed.h',
      'gay-precision.cc',
      'gay-precision.h',
      'gay-shortest.cc',
      'gay-shortest.h',
      'heap/heap-tester.h',
      'heap/heap-utils.cc',
      'heap/heap-utils.h',
      'heap/test-alloc.cc',
      'heap/test-array-buffer-tracker.cc',
      'heap/test-compaction.cc',
      'heap/test-concurrent-marking.cc',
      'heap/test-embedder-tracing.cc',
      'heap/test-heap.cc',
      'heap/test-incremental-marking.cc',
      'heap/test-invalidated-slots.cc',
      'heap/test-lab.cc',
      'heap/test-mark-compact.cc',
      'heap/test-page-promotion.cc',
      'heap/test-spaces.cc',
      'interpreter/interpreter-tester.cc',
      'interpreter/interpreter-tester.h',
      'interpreter/source-position-matcher.cc',
      'interpreter/source-position-matcher.h',
      'interpreter/test-bytecode-generator.cc',
      'interpreter/test-interpreter.cc',
      'interpreter/test-interpreter-intrinsics.cc',
      'interpreter/test-source-positions.cc',
      'interpreter/bytecode-expectations-printer.cc',
      'interpreter/bytecode-expectations-printer.h',
      'libplatform/test-tracing.cc',
      'libsampler/test-sampler.cc',
      'parsing/test-parse-decision.cc',
      'parsing/test-preparser.cc',
      'parsing/test-scanner-streams.cc',
      'parsing/test-scanner.cc',
      'print-extension.cc',
      'print-extension.h',
      'profiler-extension.cc',
      'profiler-extension.h',
      'scope-test-helper.h',
      'setup-isolate-for-tests.cc',
      'setup-isolate-for-tests.h',
      'test-access-checks.cc',
      'test-accessor-assembler.cc',
      'test-accessors.cc',
      'test-allocation.cc',
      'test-api.cc',
      'test-api.h',
      'test-api-accessors.cc',
      'test-api-interceptors.cc',
      'test-array-list.cc',
      'test-atomicops.cc',
      'test-bignum.cc',
      'test-bignum-dtoa.cc',
      'test-bit-vector.cc',
      'test-circular-queue.cc',
      'test-code-layout.cc',
      'test-code-stub-assembler.cc',
      'test-compiler.cc',
      'test-constantpool.cc',
      'test-conversions.cc',
      'test-cpu-profiler.cc',
      'test-date.cc',
      'test-debug.cc',
      'test-decls.cc',
      'test-deoptimization.cc',
      'test-dictionary.cc',
      'test-diy-fp.cc',
      'test-double.cc',
      'test-dtoa.cc',
      'test-elements-kind.cc',
      'test-fast-dtoa.cc',
      'test-feedback-vector.cc',
      'test-feedback-vector.h',
      'test-field-type-tracking.cc',
      'test-fixed-dtoa.cc',
      'test-flags.cc',
      'test-func-name-inference.cc',
      'test-global-handles.cc',
      'test-global-object.cc',
      'test-hashcode.cc',
      'test-hashmap.cc',
      'test-heap-profiler.cc',
      'test-identity-map.cc',
      'test-intl.cc',
      'test-inobject-slack-tracking.cc',
      'test-liveedit.cc',
      'test-lockers.cc',
      'test-log.cc',
      'test-managed.cc',
      'test-mementos.cc',
      'test-modules.cc',
      'test-object.cc',
      'test-orderedhashtable.cc',
      'test-parsing.cc',
      'test-platform.cc',
      'test-profile-generator.cc',
      'test-random-number-generator.cc',
      'test-regexp.cc',
      'test-representation.cc',
      'test-sampler-api.cc',
      'test-serialize.cc',
      'test-strings.cc',
      'test-symbols.cc',
      'test-strtod.cc',
      'test-thread-termination.cc',
      'test-threads.cc',
      'test-trace-event.cc',
      'test-traced-value.cc',
      'test-transitions.cc',
      'test-transitions.h',
      'test-typedarrays.cc',
      'test-types.cc',
      'test-unbound-queue.cc',
      'test-unboxed-doubles.cc',
      'test-unscopables-hidden-prototype.cc',
      'test-usecounters.cc',
      'test-utils.cc',
      'test-version.cc',
      'test-weakmaps.cc',
      'test-weaksets.cc',
      'trace-extension.cc',
      'trace-extension.h',
      'types-fuzz.h',
      'unicode-helpers.h',
      'wasm/test-c-wasm-entry.cc',
      'wasm/test-streaming-compilation.cc',
      'wasm/test-run-wasm.cc',
      'wasm/test-run-wasm-64.cc',
      'wasm/test-run-wasm-asmjs.cc',
      'wasm/test-run-wasm-atomics.cc',
      'wasm/test-run-wasm-interpreter.cc',
      'wasm/test-run-wasm-js.cc',
      'wasm/test-run-wasm-module.cc',
      'wasm/test-run-wasm-relocation.cc',
      'wasm/test-run-wasm-simd.cc',
      'wasm/test-wasm-breakpoints.cc',
      "wasm/test-wasm-codegen.cc",
      'wasm/test-wasm-interpreter-entry.cc',
      'wasm/test-wasm-stack.cc',
      'wasm/test-wasm-trap-position.cc',
      'wasm/wasm-run-utils.cc',
      'wasm/wasm-run-utils.h',
    ],
    'cctest_sources_ia32': [
      'test-assembler-ia32.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-ia32.cc',
      'test-disasm-ia32.cc',
      'test-log-stack-tracer.cc',
      'test-run-wasm-relocation-ia32.cc',
    ],
    'cctest_sources_x64': [
      'test-assembler-x64.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-x64.cc',
      'test-disasm-x64.cc',
      'test-macro-assembler-x64.cc',
      'test-log-stack-tracer.cc',
      'test-run-wasm-relocation-x64.cc',
    ],
    'cctest_sources_arm': [
      'assembler-helper-arm.cc',
      'assembler-helper-arm.h',
      'test-assembler-arm.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-arm.cc',
      'test-disasm-arm.cc',
      'test-macro-assembler-arm.cc',
      'test-run-wasm-relocation-arm.cc',
      'test-sync-primitives-arm.cc',
    ],
    'cctest_sources_arm64': [
      'test-utils-arm64.cc',
      'test-utils-arm64.h',
      'test-assembler-arm64.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-arm64.cc',
      'test-disasm-arm64.cc',
      'test-fuzz-arm64.cc',
      'test-javascript-arm64.cc',
      'test-js-arm64-variables.cc',
      'test-run-wasm-relocation-arm64.cc',
      'test-sync-primitives-arm64.cc',
    ],
    'cctest_sources_s390': [
      'test-assembler-s390.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-disasm-s390.cc',
    ],
    'cctest_sources_ppc': [
      'test-assembler-ppc.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-disasm-ppc.cc',
    ],
    'cctest_sources_mips': [
      'test-assembler-mips.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-mips.cc',
      'test-disasm-mips.cc',
      'test-macro-assembler-mips.cc',
    ],
    'cctest_sources_mipsel': [
      'test-assembler-mips.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-mips.cc',
      'test-disasm-mips.cc',
      'test-macro-assembler-mips.cc',
    ],
    'cctest_sources_mips64': [
      'test-assembler-mips64.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-mips64.cc',
      'test-disasm-mips64.cc',
      'test-macro-assembler-mips64.cc',
    ],
    'cctest_sources_mips64el': [
      'test-assembler-mips64.cc',
      'test-code-stubs.cc',
      'test-code-stubs.h',
      'test-code-stubs-mips64.cc',
      'test-disasm-mips64.cc',
      'test-macro-assembler-mips64.cc',
    ],
  },
  'includes': ['../../gypfiles/toolchain.gypi', '../../gypfiles/features.gypi'],
  'targets': [
    {
      'target_name': 'cctest',
      'type': 'executable',
      'dependencies': [
        'resources',
        '../../gypfiles/v8.gyp:v8_libbase',
        '../../gypfiles/v8.gyp:v8_libplatform',
      ],
      'include_dirs': [
        '../..',
      ],
      'sources': [
        '../common/wasm/flag-utils.h',
        '../common/wasm/test-signatures.h',
        '../common/wasm/wasm-macro-gen.h',
        '../common/wasm/wasm-module-runner.cc',
        '../common/wasm/wasm-module-runner.h',
        '<@(cctest_sources)',
        '<(generated_file)',
      ],
      'conditions': [
        ['v8_target_arch=="ia32"', {
          'sources': [
            '<@(cctest_sources_ia32)',
          ],
        }],
        ['v8_target_arch=="x64"', {
          'sources': [
            '<@(cctest_sources_x64)',
          ],
        }],
        ['v8_target_arch=="arm"', {
          'sources': [
            '<@(cctest_sources_arm)',
          ],
        }],
        ['v8_target_arch=="arm64"', {
          'sources': [
            '<@(cctest_sources_arm64)',
          ],
        }],
        ['v8_target_arch=="s390"', {
          'sources': [
            '<@(cctest_sources_s390)',
          ],
        }],
        ['v8_target_arch=="s390x"', {
          'sources': [
            '<@(cctest_sources_s390)',
          ],
        }],
        ['v8_target_arch=="ppc"', {
          'sources': [
            '<@(cctest_sources_ppc)',
          ],
        }],
        ['v8_target_arch=="ppc64"', {
          'sources': [
            '<@(cctest_sources_ppc)',
          ],
        }],
        ['v8_target_arch=="mips"', {
          'sources': [
            '<@(cctest_sources_mips)',
          ],
        }],
        ['v8_target_arch=="mipsel"', {
          'sources': [
            '<@(cctest_sources_mipsel)',
          ],
        }],
        ['v8_target_arch=="mips64"', {
          'sources': [
            '<@(cctest_sources_mips64)',
          ],
        }],
        ['v8_target_arch=="mips64el"', {
          'sources': [
            '<@(cctest_sources_mips64el)',
          ],
        }],
        [ 'OS=="win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              # MSVS wants this for gay-{precision,shortest}.cc.
              'AdditionalOptions': ['/bigobj'],
            },
          },
        }],
        ['v8_target_arch=="ppc" or v8_target_arch=="ppc64" \
          or v8_target_arch=="arm" or v8_target_arch=="arm64" \
          or v8_target_arch=="s390" or v8_target_arch=="s390x" \
          or v8_target_arch=="mips" or v8_target_arch=="mips64" \
          or v8_target_arch=="mipsel" or v8_target_arch=="mips64el"', {
          # disable fmadd/fmsub so that expected results match generated code in
          # RunFloat64MulAndFloat64Add1 and friends.
          'cflags': ['-ffp-contract=off'],
        }],
        ['OS=="aix"', {
          'ldflags': [ '-Wl,-bbigtoc' ],
        }],
        ['component=="shared_library"', {
          # cctest can't be built against a shared library, so we need to
          # depend on the underlying static target in that case.
          'dependencies': ['../../gypfiles/v8.gyp:v8_maybe_snapshot'],
          'defines': [ 'BUILDING_V8_SHARED', ]
        }, {
          'dependencies': ['../../gypfiles/v8.gyp:v8'],
        }],
        ['v8_use_snapshot=="true"', {
          'dependencies': ['../../gypfiles/v8.gyp:v8_initializers'],
        }],
      ],
    },
    {
      'target_name': 'resources',
      'type': 'none',
      'variables': {
        'file_list': [
           '../../tools/splaytree.js',
           '../../tools/codemap.js',
           '../../tools/csvparser.js',
           '../../tools/consarray.js',
           '../../tools/profile.js',
           '../../tools/profile_view.js',
           '../../tools/arguments.js',
           '../../tools/logreader.js',
           'log-eq-of-logging-and-traversal.js',
        ],
      },
      'actions': [
        {
          'action_name': 'js2c',
          'inputs': [
            '../../tools/js2c.py',
            '<@(file_list)',
          ],
          'outputs': [
            '<(generated_file)',
          ],
          'action': [
            'python',
            '../../tools/js2c.py',
            '<@(_outputs)',
            'TEST',  # type
            '<@(file_list)',
          ],
        }
      ],
    },
    {
      'target_name': 'generate-bytecode-expectations',
      'type': 'executable',
      'dependencies': [
        '../../gypfiles/v8.gyp:v8',
        '../../gypfiles/v8.gyp:v8_libbase',
        '../../gypfiles/v8.gyp:v8_libplatform',
      ],
      'include_dirs+': [
        '../..',
      ],
      'sources': [
        'interpreter/bytecode-expectations-printer.cc',
        'interpreter/bytecode-expectations-printer.h',
        'interpreter/generate-bytecode-expectations.cc',
      ],
    },
  ],
  'conditions': [
    ['test_isolation_mode != "noop"', {
      'targets': [
        {
          'target_name': 'cctest_exe_run',
          'type': 'none',
          'dependencies': [
            'cctest',
          ],
          'includes': [
            '../../gypfiles/isolate.gypi',
          ],
          'sources': [
            'cctest_exe.isolate',
          ],
        },
        {
          'target_name': 'cctest_run',
          'type': 'none',
          'dependencies': [
            'cctest_exe_run',
          ],
          'includes': [
            '../../gypfiles/isolate.gypi',
          ],
          'sources': [
            'cctest.isolate',
          ],
        },
      ],
    }],
  ],
}
