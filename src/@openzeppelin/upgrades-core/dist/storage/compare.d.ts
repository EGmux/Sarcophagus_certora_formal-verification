import { Operation } from '../levenshtein';
import { ParsedTypeDetailed, StorageItem as _StorageItem } from './layout';
import { StructMember as _StructMember } from './layout';
import { LayoutCompatibilityReport } from './report';
export declare type StorageItem = _StorageItem<ParsedTypeDetailed>;
declare type StructMember = _StructMember<ParsedTypeDetailed>;
export declare type StorageField = StorageItem | StructMember;
export declare type StorageOperation<F extends StorageField> = Operation<F, StorageFieldChange<F>>;
export declare type EnumOperation = Operation<string, {
    kind: 'replace';
    original: string;
    updated: string;
}>;
declare type StorageFieldChange<F extends StorageField> = ({
    kind: 'replace' | 'rename';
} | {
    kind: 'typechange';
    change: TypeChange;
}) & {
    original: F;
    updated: F;
};
export declare type TypeChange = ({
    kind: 'obvious mismatch' | 'unknown' | 'array grow' | 'array shrink' | 'array dynamic' | 'enum resize' | 'missing members' | 'mapping key';
} | {
    kind: 'mapping value' | 'array value';
    inner: TypeChange;
} | {
    kind: 'enum members';
    ops: EnumOperation[];
} | {
    kind: 'struct members';
    ops: StorageOperation<StructMember>[];
    allowAppend: boolean;
}) & {
    original: ParsedTypeDetailed;
    updated: ParsedTypeDetailed;
};
export declare class StorageLayoutComparator {
    readonly unsafeAllowCustomTypes: boolean;
    hasAllowedUncheckedCustomTypes: boolean;
    stack: Set<string>;
    cache: Map<string, ({
        kind: "unknown" | "obvious mismatch" | "array grow" | "array shrink" | "array dynamic" | "enum resize" | "missing members" | "mapping key";
    } & {
        original: ParsedTypeDetailed;
        updated: ParsedTypeDetailed;
    }) | ({
        kind: "mapping value" | "array value";
        inner: TypeChange;
    } & {
        original: ParsedTypeDetailed;
        updated: ParsedTypeDetailed;
    }) | ({
        kind: "enum members";
        ops: Operation<string, {
            kind: "replace";
            original: string;
            updated: string;
        }>[];
    } & {
        original: ParsedTypeDetailed;
        updated: ParsedTypeDetailed;
    }) | ({
        kind: "struct members";
        ops: Operation<StructMember, StorageFieldChange<StructMember>>[];
        allowAppend: boolean;
    } & {
        original: ParsedTypeDetailed;
        updated: ParsedTypeDetailed;
    }) | undefined>;
    constructor(unsafeAllowCustomTypes?: boolean);
    compareLayouts(original: StorageItem[], updated: StorageItem[]): LayoutCompatibilityReport;
    private layoutLevenshtein;
    getFieldChange<F extends StorageField>(original: F, updated: F): StorageFieldChange<F> | undefined;
    getTypeChange(original: ParsedTypeDetailed, updated: ParsedTypeDetailed, { allowAppend }: {
        allowAppend: boolean;
    }): TypeChange | undefined;
    private uncachedGetTypeChange;
}
export {};
//# sourceMappingURL=compare.d.ts.map